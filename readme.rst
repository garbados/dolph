Dolph
=====

Dolph is an machine translator between languages spoken by dolphins, and
arbitrary languages spoken by humans.

Based on `gensim`_, `echoprint-codegen`_, and `NLTK`_, Dolph uses `word
embedding`_ to map language artifacts like words and phrases into a
common space, such that the nearest neighbors of a particular term
within that space will have similar meanings, even across languages.

This project operates on the hypothesis that *dolphin communication can
be translated and understood*. If the project succeeds in meaningfully
translating across the languages of these different species, it will
provide evidence that dolphin communication is language, and that
language is not a phenomenon limited to humans.

How It Works
------------

Given a sufficiently large library of dolphins making noise, `echoprint-codegen` converts these sounds to codes, which we trawl for patterns of varying sizes. Then, we split the sounds in our library into arrays of known elements, and pipe those arrays to `gensim` which maps the patterns into an N-dimensional space based on their co-occurrence.

Once we map dolphin sound patterns into this space, we can do the same for corpuses from human languages, overlaying them into the same space. Then, words and sentences can be translated to and from any language mapped into the space by converting them into their nearest neighbor in the target language.

Install
-------

TODO

Usage
------

TODO

Test
----

TODO

License
-------

`ISC`_, yo.

.. _gensim: https://radimrehurek.com/gensim/
.. _echoprint-codegen: https://github.com/echonest/echoprint-codegen
.. _NLTK: http://www.nltk.org/
.. _word embedding: https://en.wikipedia.org/wiki/Word_embedding
.. _ISC: http://opensource.org/licenses/ISC
