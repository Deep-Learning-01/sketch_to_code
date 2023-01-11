

import sys
from detectron2.engine import default_setup
from detectron2.engine import default_argument_parser
from detectron2.config import get_cfg

from src.exception import SketchtocodeException



def setup_config(trained_model_config_file_path,
                weights_path ):
        """
            Create configs and perform basic setups.
        """
        try:
            parser = default_argument_parser()
            config_args = f"--config-file {trained_model_config_file_path} MODEL.WEIGHTS {weights_path}"
            args = parser.parse_args(config_args.split())


            config = get_cfg()
            config.merge_from_file(args.config_file)
            config.merge_from_list(args.opts)
            config.freeze()
            default_setup(config, args)
          
            
            return config
        except Exception as e:
            raise SketchtocodeException(e,sys)



    
