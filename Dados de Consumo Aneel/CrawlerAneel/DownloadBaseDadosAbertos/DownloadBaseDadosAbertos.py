#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from datetime import datetime
from tqdm import tqdm
tqdm.pandas()
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from RequestHelper import RequestHelper
from io import BytesIO

class DownloadBaseDadosAbertos():
    
    def setar_params(self, resource_id, storage_handler, url ,limit = 1000):
        self.resource_id = resource_id
        self.limit = limit
        self.storage_handler = storage_handler
        self.url = url
    
    def baixar_base(self):
        
        total_records = DownloadBaseDadosAbertos.obter_dados_api(resource_id = self.resource_id, limit = 1 , offset =0, url = self.url)['result']['total']

        resultados = []
        n_passos = int(np.ceil(total_records/self.limit))
        lista_offsets = np.arange(n_passos)*self.limit
        
        string_data_atual = datetime.now().date().isoformat()
        params_lista = []
        for i in range(lista_offsets.shape[0]):
            param = {}
            param['offset'] = lista_offsets[i]
            param['sufixo'] = string_data_atual
            param['limit'] = self.limit
            param['resource_id'] = self.resource_id
            param['storage_handler'] = self.storage_handler
            param['url'] = self.url
            params_lista.append(param)

        executor = ThreadPoolExecutor(max_workers=10)
        generator = executor.map(DownloadBaseDadosAbertos.obter_e_salvar_records_api_dict, params_lista)   

        for resultado in tqdm(generator, total=lista_offsets.shape[0]):
            resultados.append(resultado)
          
    @staticmethod
    def obter_e_salvar_records_api_dict( dict_param):
        
        offset = dict_param['offset']
        limit = dict_param['limit']
        sufixo = dict_param['sufixo']
        resource_id = dict_param['resource_id']
        storage_handler = dict_param['storage_handler']
        url = dict_param['url']

        return DownloadBaseDadosAbertos.obter_e_salvar_records_api(resource_id = resource_id, limit = limit, offset = offset, sufixo = sufixo, storage_handler = storage_handler , url = url )

    @staticmethod
    def obter_e_salvar_records_api(resource_id, limit ,offset, sufixo , storage_handler, url):

        path = resource_id
        if sufixo is not None:
            path += '-'+sufixo
               
        path += '\particao_' + str(int(offset/limit))+'.csv'
        sucess = False
        try:
            records = DownloadBaseDadosAbertos.obter_records_api(resource_id = resource_id , limit = limit,  offset = offset, url = url)
            if records is not None:
                df = pd.DataFrame(records)
                buffer = BytesIO()
                df.to_csv(buffer, index = False)
                storage_handler.save(path = path, buffer = buffer)
                sucess = True
                df = None
                records = None
        except:
            raise      

        if sucess:
            string_sucess = 'sucess'
        else:
            string_sucess = 'error'


        return {offset : string_sucess}

    @staticmethod
    def obter_records_api(resource_id, limit ,offset , url):
        r = DownloadBaseDadosAbertos.obter_dados_api(resource_id = resource_id , limit = limit,  offset = offset, url = url)

        records = None
        if r is not None:
            records = r['result']['records']
        return records

    @staticmethod      
    def obter_dados_api( resource_id, limit ,offset, url):
        data =  {
            "resource_id":resource_id,
            "q":"",
            "filters":{},
            "limit":limit,
            "offset":offset,
            "total_estimation_threshold":1000} 

        req_helper = RequestHelper()

        def callback(resp_json):
            k = resp_json['result']['records']

        resp, erro_no_request= req_helper.do_request(url, data=data, type_req = 'post', callback = callback, verify = True)
        #print(resp)
        #print(url)
        #print(data)
        if erro_no_request:
            resp = None
        return resp


    
