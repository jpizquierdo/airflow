# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from __future__ import annotations

from airflow.providers.google.cloud.links.base import BaseGoogleLink

DATASTORE_BASE_LINK = "/datastore"
DATASTORE_IMPORT_EXPORT_LINK = DATASTORE_BASE_LINK + "/import-export?project={project_id}"
DATASTORE_EXPORT_ENTITIES_LINK = "/storage/browser/{bucket_name}/{export_name}?project={project_id}"
DATASTORE_ENTITIES_LINK = DATASTORE_BASE_LINK + "/entities/query/kind?project={project_id}"


class CloudDatastoreImportExportLink(BaseGoogleLink):
    """Helper class for constructing Cloud Datastore Import/Export Link."""

    name = "Import/Export Page"
    key = "import_export_conf"
    format_str = DATASTORE_IMPORT_EXPORT_LINK


class CloudDatastoreEntitiesLink(BaseGoogleLink):
    """Helper class for constructing Cloud Datastore Entities Link."""

    name = "Entities"
    key = "entities_conf"
    format_str = DATASTORE_ENTITIES_LINK
