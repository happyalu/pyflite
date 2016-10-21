%module pyflite
%{
  typedef struct  cst_wave_struct {
    const char *type;
    int sample_rate;
    int num_samples;
    int num_channels;
    short *samples;
  } cst_wave;

  int init();
  void* select_voice(const char* path);
  cst_wave* text_to_wave(const char* text, void* voice);
%}

typedef struct  cst_wave_struct {
  const char *type;
  int sample_rate;
  int num_samples;
  int num_channels;
  short *samples;
} cst_wave;

%typemap (out) cst_wave* {
  if ($1 == NULL) {
    $result = Py_None;
  } else {
    $result = PyDict_New();
    PyObject *type = Py_None;
    if ($1->type) {
      type = PyString_FromString($1->type);
    }
    PyDict_SetItemString($result, "type", type);
    PyDict_SetItemString($result, "sample_rate", PyInt_FromLong((long)$1->sample_rate));
    PyDict_SetItemString($result, "num_channels", PyInt_FromLong((long)$1->num_channels));

    PyObject *list = PyList_New($1->num_samples);
    for (int i=0; i<$1->num_samples; i++) {
      PyList_SetItem(list, i, PyInt_FromLong((long)$1->samples[i]));
    }

    PyDict_SetItemString($result, "samples", list);

    delete_wave($1);
  }
 }

int init();
void* select_voice(const char* path);
cst_wave* text_to_wave(const char* text, void* voice);
