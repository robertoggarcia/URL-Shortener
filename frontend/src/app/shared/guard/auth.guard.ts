import { CanActivate } from '@angular/router';
import { Injectable } from '@angular/core';
import { Location } from '@angular/common';
import { Router, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { Observable } from 'rxjs/Observable';
import 'rxjs/Rx';
import { of } from 'rxjs';

import { ApiService } from '../api/index';

@Injectable()
export class AuthGuard implements CanActivate {

  constructor(private router: Router, private apiService: ApiService, private _location: Location) {
  }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {

	if(this.apiService.isLoggedIn()){
		return of(true); 
	} else {
		this.router.navigate(['/login']);
		return of(false);
	}
  }
}
