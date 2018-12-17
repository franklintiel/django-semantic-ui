import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="django_semantic_ui",
    version="1.0.3",
    author="Franklin Sarmiento",
    author_email="franklinitiel@gmail.com",
    description="Library to easy install, configure and use Semantic UI framework with Django project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/franklintiel/django-semantic-ui/wiki",
    license="MIT",
    classifiers=[
        #"Development Status :: 4 - Beta",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
    ],
    keywords="semantic-ui semanticui semantic ui, django-semantic-ui django-semanticui django-semantic-ui",
    project_urls={
        'Documentation': "https://github.com/franklintiel/django-semantic-ui",
        'Source': "https://github.com/franklintiel/django-semantic-ui",
        'Tracker': "https://github.com/franklintiel/django-semantic-ui/issues"
    },
    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests*']),
    python_requires=">=2.*")
