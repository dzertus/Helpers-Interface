#!/usr/bin/env python3

import logging

from ui.view_cls import DefaultInterface
from ui.btn_cls import ToolButton
from ui.cls import WidgetStack
from third_party.errors import *

logger = logging.getLogger('handler_cls')

class Handler():
    def __init__(self, model):
        super().__init__()

        logger.debug('Initialize Handler')
        self.model = model

    def add_item(self, item):
        """
        Fill Model and Ui using Script Instance
        :param item:
        :return:
        """
        self.model.add(item) # Data model
        self.add_btn(item) # Ui

    def add_btn(self, item):
        """
        Creates button for the normal view
        Generates the advanced view for the button
        :param item: (model_abstract.ScriptAbstract)
        :return:
        """
        # Create button
        btn = self.create_btn(item)
        self.default_view.add_btn(btn)

    def create_btn(self, item):
        """
        Creates a button , creates adv view for the button and sets adv view attribute
        :param item:
        :return: ToolButton
        """
        btn = ToolButton()
        btn.add_item(item)
        btn.set_handler(self)
        return btn

    def gen_adv_view_for_btn(self, btn):
        # advanced view
        btn.gen_adv_view()
        btn.adv_view.add_widget_stack(btn.widget_stack)
        btn.set_advanced_view(btn.adv_view)

    def switch_view(self, btn):
        """
        Switch between Default and Advanced views
        :param btn: :ToolButton
        :return:
        """
        if btn.adv_mod == False:
            pass # Switch to advanced
        else:
            pass # Switch to normal

    def run(self):
        """
        Run the main Ui
        :return:
        """
        logger.debug('Initializing GUI')
        self.default_view = DefaultInterface()
        self.default_view.show()
        logger.debug('GUI Initialized')

