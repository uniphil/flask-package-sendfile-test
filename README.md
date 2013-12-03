Two apps are here, to show a difference in how the `flask.helpers.send_from_directory` function works for module apps vs package apps.

### Test 1: Correct behavior with a [module app](module_app.py):

`$ python module_app.py`

```bash
$ curl http://localhost:5000
sup module app
$ 
```

Test 1 sends the file ([`module_sendfrom_dir/sendme_module.txt`](module_sendfrom_dir/sendme_module.txt)) as expected.


### Test 2: File not found with a [package app](package_app/__init__.py):

`$ python run_package_app.py`

```bash
$ curl http://localhost:5000
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
$ 
```

Test 2 `404`s; can't find the file ([`package_app/package_sendfrom_dir/sendme_package.txt`](package_app/package_sendfrom_dir/sendme_package.txt)).


### Test 3: That was weird, try adding the package directory to the `send_from_directory` call.

`$ python run_package_app.py`

```bash
$ curl http://localhost:5000/from-up-one
[a lot of html error markup]
<!--

Traceback (most recent call last):
  File "/home/phil/.virtualenvs/flask-package-sendfile-test/lib/python2.7/site-packages/flask/app.py", line 1836, in __call__
    return self.wsgi_app(environ, start_response)
  File "/home/phil/.virtualenvs/flask-package-sendfile-test/lib/python2.7/site-packages/flask/app.py", line 1820, in wsgi_app
    response = self.make_response(self.handle_exception(e))
  File "/home/phil/.virtualenvs/flask-package-sendfile-test/lib/python2.7/site-packages/flask/app.py", line 1403, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/home/phil/.virtualenvs/flask-package-sendfile-test/lib/python2.7/site-packages/flask/app.py", line 1817, in wsgi_app
    response = self.full_dispatch_request()
  File "/home/phil/.virtualenvs/flask-package-sendfile-test/lib/python2.7/site-packages/flask/app.py", line 1477, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/home/phil/.virtualenvs/flask-package-sendfile-test/lib/python2.7/site-packages/flask/app.py", line 1381, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/home/phil/.virtualenvs/flask-package-sendfile-test/lib/python2.7/site-packages/flask/app.py", line 1475, in full_dispatch_request
    rv = self.dispatch_request()
  File "/home/phil/.virtualenvs/flask-package-sendfile-test/lib/python2.7/site-packages/flask/app.py", line 1461, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/phil/code/flask-package-sendfile-test/package_app/__init__.py", line 11, in hello_package2
    return send_from_directory('package_app/package_sendfrom_dir', 'sendme_package.txt')
  File "/home/phil/.virtualenvs/flask-package-sendfile-test/lib/python2.7/site-packages/flask/helpers.py", line 616, in send_from_directory
    return send_file(filename, **options)
  File "/home/phil/.virtualenvs/flask-package-sendfile-test/lib/python2.7/site-packages/flask/helpers.py", line 520, in send_file
    file = open(filename, 'rb')
IOError: [Errno 2] No such file or directory: '/home/phil/code/flask-package-sendfile-test/package_app/package_app/package_sendfrom_dir/sendme_package.txt'

-->
$ 
```

Test 3 raises an `IOError`, because it's trying to open a path with a double `package_app` in the path :(
