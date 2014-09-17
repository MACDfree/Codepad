import sublime, sublime_plugin

filetypeMap = {
    'c':'C',
    'cpp':'C++',
    'lua':'Lua',
    'php':'PHP',
    'py':'Python'
}

class CompilerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        #print(self.view.size())
        code = self.view.substr(sublime.Region(0, self.view.size()))
        #print(code)
        lang = filetypeMap[self.view.file_name().split('.')[-1]]
        #print(filetype)

        data = {
            'code':code,
            'lang':lang,
            'submit':'Submit',
            'run':True
        }

        import urllib.request
        with urllib.request.urlopen('http://codepad.org', urllib.parse.urlencode(data).encode('utf8')) as url:
            s = url.geturl()
        #print(s)

        f = urllib.request.urlopen(s)
        b = f.read()
        f.close()
        b = b.decode('utf8')

        import re
        t1 = re.compile(r'<table border="0" cellpadding="10" cellspacing="0">([\s\S]*?)</table>')
        c1 = t1.findall(b)[0]
        t2 = re.compile(r'<pre>([\s\S]*?)</pre>')
        c1 = t2.findall(c1)[1]
        content = re.sub(r'<a[\s\S]*?>|</a>', '', c1)
        print('\n\n\n##output##')
        print(content)
        print('##########')

