from distutils.core import setup


setup(name="Live Response",
      version="0.2.2",
      description="Cross Platform Live Response Desktop application",
      license="GPL",
      author="Kayako Development Team",
      author_email="ravinder.singh@kayako.com",
      url="http://sourceforge.net/projects/pyliveresponse",
      packages = ['lrmodules'],
      scripts=['liveresponse'],
      data_files=[('resources',['resources/lr.png'])]

     )
