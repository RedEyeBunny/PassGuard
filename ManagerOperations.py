class ManagerOperations:
    def copy_random_password(self, screen_name, widget):
        if widget.winfo_class()=='Text':
            text = widget.get('1.0','end-1c')
        else:
            raise ValueError('Unsupported widget type')

        screen_name.clipboard_append(text)
