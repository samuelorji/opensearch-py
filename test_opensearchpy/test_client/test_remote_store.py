# -*- coding: utf-8 -*-
# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.
from test_opensearchpy.test_cases import OpenSearchTestCase


class TestRemoteStore(OpenSearchTestCase):
    def test_remote_store_restore(self) -> None:
        self.client.remote_store.restore(body=["index-1"])
        self.assert_url_called("POST", "/_remotestore/_restore")
