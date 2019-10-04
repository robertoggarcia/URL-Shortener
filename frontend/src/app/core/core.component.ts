import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../shared/api/index';

@Component({
  selector: 'app-core',
  templateUrl: './core.component.html',
  styleUrls: ['./core.component.css']
})
export class CoreComponent implements OnInit {
	url = '';
	invalid = false;
	short_url = ''
	errors = false;

  constructor(private api: ApiService) { }

  ngOnInit() {
  }

  generateUrl() {
  	this.invalid = false;
  	const URL_REGEXP = /^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$/;  
      
    const valid_url = URL_REGEXP.test(this.url);
    if (!valid_url) {
    	this.invalid = true;
    	return;
    }

    this.api.generateUrl(this.url).subscribe(res => {
    	this.invalid = false;
    	this.short_url = res['short_url'];
    	this.url = '';
    }, err => {
    	this.errors = true;
    })
  	
  }
}