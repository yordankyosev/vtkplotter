# Work with vtkVolume objects (voxel datasets) and surfaces.
#
from vtkplotter import vtkio, utils, Plotter

vp = Plotter()

# Load a 3D voxel dataset (returns a vtkImageData object):
img = vtkio.loadImageData('data/embryo.slc', spacing=[1,1,1])

# Build a vtkVolume object. 
# A set of transparency values - of any length - can be passed
# to define the opacity transfer function in the range of the scalar.
#  E.g.: setting alphas=[0, 0, 0, 1, 0, 0, 0] would make visible
#  only voxels with value close to 98.5 (see print output).
vol = utils.makeVolume(img, c='green', alphas=[0, 0.4, 0.9, 1]) 

sph = vp.sphere(pos=[100,100,100], r=20) # add a dummy surface

vp.show([vol, sph], zoom=1.4) # show both vtkVolume and vtkActor




