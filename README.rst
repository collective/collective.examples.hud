=======================
collective.examples.hud
=======================

Plone Heads Up Display Panel Example

* `Source code @ GitHub <https://github.com/collective/collective.examples.hud>`_


How to make your own panels?
============================

Guidelines
----------

* Add plone.hud as dependency `see here <https://github.com/collective/collective.examples.hud/blob/master/buildout.d/development.cfg#L10>`_
* Add permission for the panel `see here <https://github.com/collective/collective.examples.hud/blob/master/collective/examples/hud/configure.zcml#L25>`_
* Add view registration `see here <https://github.com/collective/collective.examples.hud/blob/master/collective/examples/hud/configure.zcml#L35>`_
* Add configlet registration `see here <https://github.com/collective/collective.examples.hud/blob/master/collective/examples/hud/profiles/default/controlpanel.xml#L7>`_
* Add view class `see here <https://github.com/collective/collective.examples.hud/blob/master/collective/examples/hud/panels.py#L7>`_
* Add template if needed `see here <https://github.com/collective/collective.examples.hud/blob/master/collective/examples/hud/first_panel.pt>`_


Development
===========

Add to your ``buildout.cfg``::

    ...
    eggs +=
        ...
        plone.hud
        collective.examples.hud
    ...
    extensions += mr.developer
    sources = sources

    auto-checkout =
        plone.hud
        collective.examples.hud

    [sources]
    plone.hud = git git://github.com/plone/plone.hud.git
    collective.examples.hud = git git://github.com/collective/collective.examples.hud.git
    ...
