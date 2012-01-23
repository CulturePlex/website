#include <boost/python.hpp>
#include <boost/cstdint.hpp>

#include <Magick++/Drawable.h>
#include <Magick++.h>

using namespace boost::python;

namespace  {

struct Magick_PathArcRel_Wrapper: Magick::PathArcRel
{
    Magick_PathArcRel_Wrapper(PyObject* py_self_, const Magick::PathArcArgs& p0):
        Magick::PathArcRel(p0), py_self(py_self_) {}

    Magick_PathArcRel_Wrapper(PyObject* py_self_, const Magick::PathArcArgsList& p0):
        Magick::PathArcRel(p0), py_self(py_self_) {}

    Magick_PathArcRel_Wrapper(PyObject* py_self_, const Magick::PathArcRel& p0):
        Magick::PathArcRel(p0), py_self(py_self_) {}


    PyObject* py_self;
};


}


void __PathArcRel()
{
    class_< Magick::PathArcRel, Magick_PathArcRel_Wrapper >("PathArcRel", init< const Magick::PathArcArgs& >())
        .def(init< const Magick::PathArcArgsList& >())
        .def(init< const Magick::PathArcRel& >())
    ;

}
