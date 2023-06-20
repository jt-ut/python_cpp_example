from pathlib import Path
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup, find_packages

class custom_build_ext(build_ext):
    def build_extensions(self):
        # Override the compiler executables. Importantly, this
        # removes the "default" compiler flags that would
        # otherwise get passed on to to the compiler, i.e.,
        # distutils.sysconfig.get_var("CFLAGS").
        #self.compiler.set_executable("compiler_so", "/usr/local/opt/llvm/bin/clang++")
        #self.compiler.set_executable("compiler_cxx", "/usr/local/opt/llvm/bin/clang++")
        #self.compiler.set_executable("linker_so", "/usr/local/opt/llvm/bin/clang++")
        #self.compiler.set_executable("compiler_so", "/usr/local/opt/gcc@12/bin/g++-12")
        #self.compiler.set_executable("compiler_cxx", "/usr/local/opt/gcc@12/bin/g++-12")
        #self.compiler.set_executable("linker_so", "/usr/local/opt/gcc@12/bin/g++-12")
        self.compiler.set_executable("compiler_so", "g++")
        self.compiler.set_executable("compiler_cxx", "g++")
        self.compiler.set_executable("linker_so", "g++")
        build_ext.build_extensions(self)

#extra_compile_args = ['-shared', '-std=c++11', '-fPIC', '-Wall', '-g', '-O3', "-arch", "x86_64"]
#extra_compile_args = ['-std=c++11', '-fPIC', '-Xpreprocessor', '-fopenmp']
extra_compile_args = ['-std=c++11', '-Xpreprocessor', '-fopenmp']

#extra_link_args = ['-dynamiclib', '-undefined', 'dynamic_lookup']
#extra_link_args = ['-bundle', '-undefined', 'dynamic_lookup']
extra_link_args = []; 

# C++ build directive 
ext_module = Pybind11Extension(
    # Name of exposed module 
    name = 'python_cpp_example._pycppex',
    # List C++ source files containing PyBind11 bindings, 
    # either all globbed, 
    #sources=[str(fname) for fname in Path('src/python_cpp_example').glob('*.cpp')],
    # or specific ones 
    sources = ['src/python_cpp_example/bindings.cpp', 'src/python_cpp_example/math.cpp'], # Source files  
    # Location of required headers for C++ source code 
    include_dirs=['/usr/local/Cellar/libomp'],
    # Build flags 
    extra_compile_args = extra_compile_args,
    extra_link_args = extra_link_args, 
)



setup(
    name='python_cpp_example',
    version='0.1',
    author='Benjamin Jack',
    author_email='benjamin.r.jack@gmail.com',
    description='A hybrid Python/C++ test project',
    long_description='',
    # tell setuptools to look for any packages under 'src'
    #packages=find_packages('src'),
    # tell setuptools that all packages will be under the 'src' directory
    # and nowhere else
    package_dir={'':'src'},
    # add an extension module named 'python_cpp_example' to the package 
    # 'python_cpp_example'
    #ext_modules=[CMakeExtension('python_cpp_example/python_cpp_example')],
    py_modules = ['_hello'], 
    ext_modules = [ext_module], 
    # add custom build_ext command
    #cmdclass=dict(build_ext=CMakeBuild),
    #cmdclass={"build_ext": build_ext},
    #cmdclass={"build_ext": custom_build_ext}, #Default build instruction via: cmdclass={"build_ext": build_ext},
    #zip_safe=False,
)

