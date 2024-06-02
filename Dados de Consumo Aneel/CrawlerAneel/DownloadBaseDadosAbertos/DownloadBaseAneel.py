#!/usr/bin/env python
# coding: utf-8

from .DownloadBaseDadosAbertos import DownloadBaseDadosAbertos

class DownloadBaseAneel(DownloadBaseDadosAbertos):

    def __init__(self, storage_handler, limit = 1000):

        lst_resource_id = ["ff80dd21-eade-4eb5-9ca8-d802c883940e","b9ad890b-d500-4294-bd36-1108acc54832","7e097631-46ad-4051-8954-9ef8fb594fdc",
                           "29f9fec9-34dd-454b-8f3c-6b4ca5b22f2c","641003d6-4e87-4095-9416-ae5fbb5c94d3", "4a84f3c8-9dc8-4448-bba8-cc2dfbc26ca2"]

        url = "https://dadosabertos.aneel.gov.br/api/3/action/datastore_search"

        for resource_id in lst_resource_id :
            super().setar_params(resource_id = resource_id, storage_handler = storage_handler, limit= limit, url= url)
            self.baixar_base()
    