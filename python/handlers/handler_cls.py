#!/usr/bin/python2

import logging

logger = logging.getLogger('handler_cls')

class Handler():
    def __init__(self, model):
        super(Handler).__init__()

        logger.debug('Initialize Handler')
        self.model = model
        self.active_view = None

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
        self.gen_adv_view_for_btn(btn)
        self.default_view.add_btn(btn)

    def create_btn(self, item):
        """
        Creates a button , creates adv view for the button and sets adv view attribute
        :param item:
        :return: ToolButton
        """
        btn = btn_cls.ToolButton()
        btn.add_item(item)
        btn.set_handler(self)
        return btn

    def gen_adv_view_for_btn(self, btn):
        """
        Generate advanced view for the button
        :param btn:
        """
        # advanced view
        btn.gen_adv_view()
        btn.set_advanced_view(btn.adv_view)
        print('Button adv view {0}'.format(btn.adv_view))

    def set_active_view(self, view):
        """
        Stores the current active view into active_view variable
        :param view:
        """
        self.active_view = view

    def switch_view(self, btn):
        """
        Switch between Default and Advanced views
        :param btn: :ToolButton
        :return:
        """
        print('switch view')
        logger.debug('Right Click on : {}'.format(btn.item.name))
        logger.debug('Active view current instance : {}'.format(type(self.active_view)))
        current_btn_index = self.default_view.container_layout.indexOf(btn)
        print(current_btn_index)

        if isinstance(self.active_view, view_cls.DefaultInterface):
            btn.adv_view.switch_view(self.default_view)
            btn.adv_view.add_btn(btn)
            self.set_active_view(btn.adv_view)
        else:
            self.default_view.switch_view(btn.adv_view)
            self.default_view.container_layout.insertWidget(current_btn_index, btn)
            self.set_active_view(self.default_view)

    def open_sources_manager_dialog(self):
        self.active_view.test()

    def run(self):
        """
        Run the main Ui
        :return:
        """
        logger.debug('Initializing GUI')
        self.default_view = view_cls.DefaultInterface()
        self.default_view.show()
        self.set_active_view(self.default_view)
        logger.debug('GUI Initialized')
