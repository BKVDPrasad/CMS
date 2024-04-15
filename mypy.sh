#!/bin/bash

# This is a sample bash file that runs mypy on your code with some options

# Use --ignore-missing-imports to ignore errors related to missing modules or packages
# Use --strict to enable all optional strictness flags
# Use --show-error-codes to display error codes for each message
mypy --ignore-missing-imports --strict --show-error-codes .

# You can also use a mypy configuration file to specify the options for different modules or packages
# See the mypy command line documentation[^1^][2] and the mypy configuration file documentation[^2^][1] for more details
mypy --config-file mypy.ini




##!/bin/bash
#
##--strict
#
##pushd `git rev-parse --show-toplevel` > /dev/null
##mapfile -t check < mypy.check
##mypy --config-file mypy.ini "${check[@]}"
##popd > /dev/null
#
#[mypy]
#plugins = mypy_django_plugin.main
#follow_imports = skip
#no_implicit_optional = True
#namespace_packages = True
#
#[mypy.plugins.django-stubs]
#django_settings_module = interfaces.control.settings
#
#[mypy-*.migrations.*]
#ignore_errors = True
#
#[mypy-*.tests.*]
#ignore_errors = True
#
## ignore dependencies which do not support type hinting / stubs
#[mypy-model_mommy.*]
#ignore_missing_imports = True
#
#[mypy-rest_framework_json_api.*]
#ignore_missing_imports = True
#
#[mypy-rest_framework.*]
#ignore_missing_imports = True
#
#[mypy-pytest.*]
#ignore_missing_imports = True
#
#[mypy-freezegun.*]
#ignore_missing_imports = True
#
#[mypy-testfixtures.*]
#ignore_missing_imports = True
#
#[mypy-easy_pdf.*]
#ignore_missing_imports = True
#
#[mypy-formtools.*]
#ignore_missing_imports = True
#
#[mypy-elasticsearch.*]
#ignore_missing_imports = True
#
#[mypy-elasticsearch_dsl.*]
#ignore_missing_imports = True
#
#[mypy-django_filters.*]
#ignore_missing_imports = True
#
#[mypy-suds.*]
#ignore_missing_imports = True
#
#[mypy-xmlrpc.*]
#ignore_missing_imports = True
#
#[mypy-isodate.*]
#ignore_missing_imports = True
#
#[mypy-tablib.*]
#ignore_missing_imports = True
#
#[mypy-django_redis.*]
#ignore_missing_imports = True
#
#[mypy-redis.*]
#ignore_missing_imports = True
#
#[mypy-kombu.*]
#ignore_missing_imports = True
#
#[mypy-jsonschema.*]
#ignore_missing_imports = True
#
#[mypy-lxml.*]
#ignore_missing_imports = True
#
#[mypy-xmltodict.*]
#ignore_missing_imports = True
#
#[mypy-jsonfield.*]
#ignore_missing_imports = True
#
#[mypy-django_extensions.db.fields.json.*]
#ignore_missing_imports = True
#
#[mypy-zeep.*]
#ignore_missing_imports = True
#
#[mypy-pdfminer.*]
#ignore_missing_imports = True
#
#[mypy-PyPDF2.*]
#ignore_missing_imports = True
#
#[mypy-reportlab.*]
#ignore_missing_imports = True
#
#[mypy-PIL.*]
#ignore_missing_imports = True
#
#[mypy-celery.*]
#ignore_missing_imports = True
#
#[mypy-fdfgen.*]
#ignore_missing_imports = True
#
#[mypy-rest_auth.models.*]
#ignore_missing_imports = True
#
#[mypy-django_auth_ldap.backend.*]
#ignore_missing_imports = True
#
#[mypy-django_password_validators.password_history.*]
#ignore_missing_imports = True
#
#[mypy-xlsxwriter]
#ignore_missing_imports = True
#
#[mypy-rest_auth.*]
#ignore_missing_imports = True
#
#[mypy-rangefilter.filter.*]
#ignore_missing_imports = True
#
#[mypy-cached_property.*]
#ignore_missing_imports = True
#
#[mypy-auth_client.*]
#ignore_missing_imports = True
#
#[mypy-simple_history.*]
#ignore_missing_imports = True
#
#[mypy-cassandra.*]
#ignore_missing_imports = True
#
#[mypy-transliterate.*]
#ignore_missing_imports = True
#
#[mypy-fitz.*]
#ignore_missing_imports = True
