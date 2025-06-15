import torch
import unittest
from zonos.model import Zonos
from zonos.config import ZonosConfig, BackboneConfig, PrefixConditionerConfig

class TestCPUExecution(unittest.TestCase):

    def test_model_loads_on_cpu(self):
        """Test that the Zonos model loads on CPU by default."""
        # Create a minimal config for a small model
        # This avoids needing to download pretrained weights for a simple device check
        backbone_config = BackboneConfig(
            d_model=32, # Small dimension
            n_layer=1   # Minimal layers
        )
        # Dummy prefix conditioner config
        prefix_conditioner_config = PrefixConditionerConfig(
            conditioners=[], # No actual conditioners
            projection="none"
        )
        config = ZonosConfig(
            backbone=backbone_config,
            prefix_conditioner=prefix_conditioner_config,
            eos_token_id=0, # Dummy value
            masked_token_id=1 # Dummy value
        )
        model = Zonos(config)
        self.assertEqual(model.device.type, "cpu")

if __name__ == '__main__':
    unittest.main()
