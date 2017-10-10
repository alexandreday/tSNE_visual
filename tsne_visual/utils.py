'''
Created on Jan 5, 2017

@author: Alexandre Day
'''

import numpy as np

def data_to_binary(X, tmp_binfile="data.dat", delimiter=None):
    """ Writes it in binary format in default file 'data.dat' for tsne c++ exec. to use.
    """
    
    #print("Saving data in %s"%tmp_binfile)
    output_file=open(tmp_binfile,'wb')
    from array import array
    float_array = array('d', X.flatten())
    float_array.tofile(output_file)
    output_file.close()

def run_tsne_command_line(parameters, default_path=".", remove = None):
    """ Run C++ exe from python with stdout output generated by exexutable printed to screen.
        By default the bh_tsne.exe should be in the current working directory
        This can be changed by choosing a different default_path
    """
    import subprocess, os, time
    import tsne_visual.utils as tmp
    
    dir_source=os.path.dirname(tmp.__file__) # trick to get the path to the executable in the package !
    
    param_str=[str(p) for p in parameters]

    subprocess.run([dir_source+'/bh_tsne']+param_str)
    #print(dir_source+'/bh_tsne'+" ".join(param_str))
    if remove is not None:
        time.sleep(0.05)
        os.system("rm "+os.getcwd()+"/"+remove)
        #subprocess.run(["rm "+os.getcwd()+"/"+remove]) # remove this file from directory
    
def generate_unique_fname(parameters):
    """Produces a file name indicating the main parameters for the t-SNE simulation
    It also attaches a unique random tag so that you can run t-SNE with the same parameters multiple times (different random seed).

    Parameter
    -------------

    parameters: dict, from str to numerical values
        Should contain the main t-SNE parameters
    """
    import uuid

    fname = "dim=%i_angle=%.2f_perp=%i_nIter=%i"%(parameters['n_components'], parameters['angle'], parameters['perplexity'], parameters['n_iter'])
    unique_tag = uuid.uuid4().hex
    return fname + "_" + unique_tag
