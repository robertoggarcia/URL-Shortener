import { Component, OnInit } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router';
import { ApiService } from '../../api/index';

@Component({
    selector: 'app-header',
    templateUrl: './header.component.html',
    styleUrls: ['./header.component.css']
})
export class HeaderComponent {
  constructor(public router: Router, private api: ApiService) {
  }
  
  ngOnInit() {
  }

  logout() {
  	this.api.logout();
  }
}
