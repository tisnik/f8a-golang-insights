#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contains the configuration for both the training and scoring parts.

Copyright © 2018 Red Hat Inc.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import os

ECOSYSTEM = os.environ.get('ARM_SCORING_REGION', 'golang')
DEPLOYMENT_PREFIX = os.environ.get('DEPLOYMENT_PREFIX', 'dev')
MODEL_VERSION = os.environ.get('MODEL_VERSION', '2019-01-03')
_TRAINING_OBJECT_PREFIX = os.path.join(ECOSYSTEM, DEPLOYMENT_PREFIX, MODEL_VERSION, "data")
_TRAINED_OBJECT_PREFIX = os.path.join(ECOSYSTEM, DEPLOYMENT_PREFIX, MODEL_VERSION, "trained-model")

AWS_S3_ACCESS_KEY_ID = os.environ.get("AWS_S3_ACCESS_KEY_ID", "")
AWS_S3_SECRET_ACCESS_KEY = os.environ.get("AWS_S3_SECRET_ACCESS_KEY", "")
S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME", "golang-insights")
AWS_S3_ENDPOINT_URL = os.environ.get("AWS_S3_ENDPOINT_URL", "")
NORMALIZED_MANIFEST_PATH = os.path.join(_TRAINING_OBJECT_PREFIX,
                                        "golang_manifests_unique.json")
PACKAGE_INGESTION_LIST = os.path.join(_TRAINING_OBJECT_PREFIX,
                                      "packages_to_ingest.txt")
ASSOCIATION_RULE_JSON = "association_rules.json"
ASSOCIATION_RULES_DF = "association_rules.pkl"
MIN_SUPPORT = float(os.environ.get("MIN_SUPPORT", 0.05))
MIN_CONFIDENCE = float(os.environ.get("MIN_CONFIDENCE", 0.40))
USE_AWS = os.environ.get("USE_AWS", "True")
PACKAGE_IDX_MAPS = "package_idx.json"
MIN_CONFIDENCE_SCORING = float(os.environ.get("MIN_CONFIDENCE_SCORING", .60))
