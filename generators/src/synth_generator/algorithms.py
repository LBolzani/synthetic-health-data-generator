from sdv.tabular import CTGAN
from sdv.tabular import CopulaGAN
from sdv.tabular import GaussianCopula
from sdv.tabular import TVAE

ctan = 'CTGAN'
copulaGan = 'CopulaGAN'
gaussianCopula = 'GaussianCopula'
tvae = 'TVAE'

algos = {ctan: CTGAN(),
         copulaGan: CopulaGAN() ,
         gaussianCopula: GaussianCopula(),
         tvae: TVAE()}