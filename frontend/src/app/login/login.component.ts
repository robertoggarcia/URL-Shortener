import { Component, OnInit, NgZone } from '@angular/core';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ApiService } from '../shared/api/index';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
	registerForm: FormGroup;
  login_error = false;
  submitted = false;

	constructor(public router: Router, private formBuilder: FormBuilder, private api: ApiService, private ngZone: NgZone) {
		this.registerForm = this.formBuilder.group({
            username: ['', [Validators.required]],
            password: ['', [Validators.required]]
        });
	}

	get f() { return this.registerForm.controls; }

	ngOnInit() {
		
	}
  login() {
    this.submitted = true;
    if (this.registerForm.invalid) {
        return;
    } else {
      const username = this.registerForm.value['username'];
      const password = this.registerForm.value['password'];
      this.api.login(username, password).subscribe(res => {
        localStorage.setItem('token', res.access);
        this.router.navigate(['/users']);
      },
        err => {
          console.log(err);
          this.login_error = true;
        }
      );
    }
  }

  saveSession(session) {
  }
}
