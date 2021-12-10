from transformers import BertTokenizer, BertModel
from ..baseExtractor import baseTextExtractor
import torch
import numpy as np


class bertExtractor(baseTextExtractor):
    """
    Text feature extractor using BERT
    Ref: https://huggingface.co/docs/transformers/model_doc/bert
    Pretrained models: https://huggingface.co/models
    """
    def __init__(self, config, logger):
        try:
            logger.info("Initializing BERT text feature extractor.")
            super().__init__(config, logger)
            self.tokenizer = BertTokenizer.from_pretrained(self.config['pretrained'])
            self.model = BertModel.from_pretrained(self.config['pretrained']).to(self.config['device'])
            self.finetune = self.config['finetune'] if 'finetune' in self.config else False
        except Exception as e:
            logger.error("Failed to initialize librosaExtractor.")
            raise e
    
    def extract(self, text):
        try:
            input_ids = self.tokenizer.encode(text, add_special_tokens=True, return_tensors='pt').to(self.config['device'])
            with torch.no_grad():
                last_hidden_state = self.model(input_ids)[0]
            return last_hidden_state.squeeze().cpu().numpy()
        except Exception as e:
            self.logger.error(f"Failed to extract text features with BERT for '{text}'.")
            raise e

    def tokenize(self, text):
        """
        For compatibility with feature files generated by MMSA DataPre.py
        Returns:
            input_ids: input_ids,
            input_mask: attention_mask,
            segment_ids: token_type_ids
        """
        try:
            input_ids = self.tokenizer.encode(text, add_special_tokens=True)
            input_ids = np.expand_dims(input_ids, 1)
            input_mask = np.ones_like(input_ids)
            segment_ids = np.zeros_like(input_ids)
            text_bert = np.concatenate([input_ids, input_mask, segment_ids], axis=1)
            return text_bert
        except Exception as e:
            self.logger.error(f"Failed to tokenize text with BERT for '{text}'.")
            raise e