#include <pybind11/pybind11.h>
#include "include/math.hpp"

namespace py = pybind11;

// int add(int i, int j)
// {
//     return i + j;
// }


// Note: the naming convention <package>._<hidden module name> is suggested here
// https://github.com/pybind/python_example/issues/26

PYBIND11_MODULE(_pycppex, m)
{
    m.attr("__name__") = "python_cpp_example._pycppex";
    //py::module m("_cpp");
    m.def("add", &add);
    m.def("subtract", &subtract);
    //return m.ptr();
}