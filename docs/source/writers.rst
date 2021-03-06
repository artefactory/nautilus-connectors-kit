#######
Writers
#######

**Writers are writing output stream records to the destination of your choice.**

*About to develop a new writer?* See the :ref:`getting_started:How to develop a new writer` section.

*Just want to use an existing writer?* This page provides you with documentation on available commands:

================
Amazon S3 Writer
================

----------
Quickstart
----------

The following command would allow you to:

- write output stream records to a blob named ``google_analytics_report_2020-01-01.njson``
- under the Amazon S3 bucket ``nck_extracts``
- organized according to the following path: ``nck_extracts/FR/google_analytics/google_analytics_report_2020-01-01.njson``

.. code-block:: shell

    write_s3 --s3-bucket-name nck_extracts --s3-prefix FR/google_analytics --s3-filename google_analytics_report_2020-01-01.njson --s3-bucket-region <BUCKET_REGION> --s3-access-key-id <ACCESS_KEY_ID> --s3-access-key-secret <ACCESS_KEY_SECRET>

------------
Command name
------------

``write_s3``

---------------
Command options
---------------

==============================  ==============================
Options                         Definition
==============================  ==============================
``--s3-bucket-name``            S3 bucket name
``--s3-prefix``                 S3 blob prefix
``--s3-filename``               S3 blob name
``--s3-bucket-region``          S3 bucket region
``--s3-access-key-id``          S3 access key ID
``--s3-access-key-secret``      S3 access key secret
==============================  ==============================

======================
Google BigQuery Writer
======================

----------
Quickstart
----------

The following command would allow you to:

- store output stream records into the BigQuery table ``google_analytics``
- located under the BigQuery dataset ``nck``

As a preliminary step, stream data would be uploaded into a temporary blob located under the Cloud Storage bucket ``nck_extracts``.

.. code-block:: shell

    write bq --bq-dataset nck --bq-table google_analytics --bq-bucket nck-extracts

------------
Command name
------------

``write_bq``

---------------
Command options
---------------

==============================  =================================================================================================================================================
Options                         Definition
==============================  =================================================================================================================================================
``--bq-dataset``                BigQuery dataset name
``--bq-table``                  BigQuery table name
``--bq-write-disposition``      BigQuery write disposition. Possible values: TRUNCATE (default), APPEND
``--bq-partition-column``       (Optional) Field to be used as a partition column (more information on `this page <https://cloud.google.com/bigquery/docs/partitioned-tables>`__)
``--bq-location``               BigQuery dataset location. Possible values: EU (default), US.
``--bq-bucket``                 Cloud Storage bucket in which stream data should be written as a first step, before being uploaded into the BigQuery destination table
``--bq-keep-files``             False (default) if Cloud Storage blob should be deleted once the data has been uploaded into the BigQuery destination table, True otherwise
==============================  =================================================================================================================================================

===========================
Google Cloud Storage Writer
===========================

----------
Quickstart
----------

The following command would allow you to:

- write output stream records to a blob named ``google_analytics_report_2020-01-01.njson``
- located under the Cloud Storage bucket ``nck_extracts``
- organized according to the following path: ``nck_extracts/FR/google_analytics/google_analytics_report_2020-01-01.njson``

.. code-block:: shell

    write_gcs --gcs-project-id <GCP_PROJECT_ID> --gcs-bucket nck_extracts --gcs-prefix FR/google_analytics --gcs-filename google_analytics_report_2020-01-01.njson

------------
Command name
------------

``write_gcs``

---------------
Command options
---------------

==============================  ==============================
Options                         Definition
==============================  ==============================
``--gcs-project-id``            GCP project ID
``--gcs-bucket``                Cloud Storage bucket name
``--gcs-prefix``                Cloud Storage blob prefix
``--gcs-file-name``             Cloud Storage blob name
==============================  ==============================

============
Local Writer
============

----------
Quickstart
----------

The following command would allow you to write a file ``google_analytics_report_2020-01-01.njson`` on the ``~/Desktop`` directory of your local machine:

.. code-block:: shell

    write_local --local-directory ~/Desktop/ --file-name google_analytics_report_2020-01-01.njson

------------
Command name
------------

``write_local``

---------------
Command options
---------------

==============================  ===============================================================
Options                         Definition
==============================  ===============================================================
``--local-directory (-d)``      Local directory in which the destination file should be stored
``--file-name (-n)``            Destination file name
==============================  ===============================================================

==============
Console Writer
==============

----------
Quickstart
----------

The following command would allow you to write stream output records directly into your terminal, which is very convenient for debugging:

.. code-block:: shell

    write_console

------------
Command name
------------

``write_console``

---------------
Command options
---------------
*This writer command expects no options.*
