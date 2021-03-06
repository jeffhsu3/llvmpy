from binding import *
from .namespace import llvm

CallingConv = llvm.Namespace('CallingConv')
ID = CallingConv.Enum('ID', '''
        C, Fast, Cold, GHC, FirstTargetCC, X86_StdCall, X86_FastCall,
        ARM_APCS, ARM_AAPCS, ARM_AAPCS_VFP, MSP430_INTR, X86_ThisCall,
        PTX_Kernel, PTX_Device, MBLAZE_INTR, MBLAZE_SVOL, SPIR_FUNC,
        SPIR_KERNEL, Intel_OCL_BI
        ''') # HiPE
