# -*- coding: utf-8 -*-
from collective.examples.hud import _
from plone.hud.panel import HUDPanelView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class FirstPanelView(HUDPanelView):
    panel_template = ViewPageTemplateFile('first_panel.pt')

    def render(self):
        return self.panel_template()


class SecondPanelView(HUDPanelView):
    panel_template = ViewPageTemplateFile('second_panel.pt')

    def render(self):
        return self.panel_template()
