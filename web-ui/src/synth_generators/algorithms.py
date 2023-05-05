from sdv.tabular import CTGAN
from sdv.tabular import CopulaGAN
from sdv.tabular import GaussianCopula
from sdv.tabular import TVAE



algos = {'CTGAN': CTGAN(),
         'CopulaGAN': CopulaGAN(),
         'GaussianCopula': GaussianCopula(),
         'TVAE': TVAE()}

arguments = ['gaussian', 'gamma', 'beta', 'student_t', 'gaussian_kde', 'truncated_gaussian']
