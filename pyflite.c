// Copyright (2016) Alok Parlikar <alok@parlikar.com>

#include "flite.h"

extern void usenglish_init(cst_voice *v);
extern cst_lexicon *cmulex_init(void);

int init() {
  int x = flite_init();
  if (x) {
    // Failed
    return x;
  }

  flite_add_lang("eng",usenglish_init,cmulex_init);
  return x;
}

void* select_voice(const char* path) {
  cst_voice *v = flite_voice_load(path);
  return (void*) v;
}

cst_wave* text_to_wave(const char* text, void* voice) {
  cst_voice* v = (cst_voice*) voice;
  if (!v) return NULL;
  return flite_text_to_wave(text, v);
}

