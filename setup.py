from cx_Freeze import setup, Executable

executables = [Executable('cooked_interface.py')]

include_files = ['model', 'my_model', 'dataset.csv', "file"]

options = {
	'build_exe': {
		'include_msvcr': True,
		'build_exe': 'build_windows',
		'include_files': include_files,
	}
}

setup(name='car_cost',
	  version='0.0.1',
	  description='Neural regression of cars cost',
	  executables=executables,
	  options=options)
