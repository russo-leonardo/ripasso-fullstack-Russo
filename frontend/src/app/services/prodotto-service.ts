import { inject, Service } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Prodotto } from '../prodotto';

@Service()
export class ProdottoService {
    private http = inject(HttpClient);
    private url = '/api/prodotti';

    getProdotti() : Observable<Prodotto[]> {
        return this.http.get<Prodotto[]>(this.url);
    }
}
