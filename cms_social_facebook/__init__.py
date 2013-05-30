import warnings
warnings.warn("The cms_social_facebook name is deprecated, you should change "
              "your imports to cms_social_networks")

import sys
import cms_social_networks
sys.modules['cms_social_facebook'] = cms_social_networks
