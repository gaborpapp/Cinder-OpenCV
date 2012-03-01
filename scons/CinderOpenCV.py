import sys

def getSources(relpath):
	return []

def getIncludes(relpath):
	_INCLUDES = ['../include']
	return [relpath + s for s in _INCLUDES]

def getLibs(relpath):
	if sys.platform == 'darwin':
		_LIBS = ['libopencv_calib3d.a', 'libopencv_contrib.a',
				'libopencv_core.a', 'libopencv_features2d.a',
				'libopencv_flann.a', 'libopencv_gpu.a',
				'libopencv_haartraining_engine.a', 'libopencv_imgproc.a',
				'libopencv_legacy.a', 'libopencv_ml.a',
				'libopencv_objdetect.a', 'libopencv_video.a']
		return [relpath + '../lib/macosx/' + s for s in _LIBS]
	else:
		return []

