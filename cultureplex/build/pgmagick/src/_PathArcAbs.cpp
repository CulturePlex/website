#include <boost/python.hpp>
#include <boost/cstdint.hpp>

#include <Magick++/Drawable.h>
#include <Magick++.h>

using namespace boost::python;

namespace  {

struct Magick_PathArcAbs_Wrapper: Magick::PathArcAbs
{
    Magick_PathArcAbs_Wrapper(PyObject* py_self_, const Magick::PathArcArgs& p0):
        Magick::PathArcAbs(p0), py_self(py_self_) {}

    Magick_PathArcAbs_Wrapper(PyObject* py_self_, const Magick::PathArcArgsList& p0):
        Magick::PathArcAbs(p0), py_self(py_self_) {}

    Magick_PathArcAbs_Wrapper(PyObject* py_self_, const Magick::PathArcAbs& p0):
        Magick::PathArcAbs(p0), py_self(py_self_) {}


    PyObject* py_self;
};


}


void __PathArcAbs()
{
    class_< Magick::PathArcAbs, Magick_PathArcAbs_Wrapper >("PathArcAbs", init< const Magick::PathArcArgs& >())
        .def(init< const Magick::PathArcArgsList& >())
        .def(init< const Magick::PathArcAbs& >())
    ;

}
