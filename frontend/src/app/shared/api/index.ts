import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Observable, throwError } from 'rxjs';
import { catchError, retry, map } from 'rxjs/operators';
import { HttpClient, HttpHeaders, HttpErrorResponse, HttpEvent, HttpEventType } from '@angular/common/http';


@Injectable()
export class ApiService {
  private host = 'http://127.0.0.1:8000/';
  private apiUrl = this.host + 'api/v1/';
  private loggedIn = false;

  constructor(private http: HttpClient, private router: Router) {
      this.loggedIn = !!localStorage.getItem('token');
  }

  login(user, pass): Observable<any> {
    const login: any = {
      grant_type: 'password',
      username: user,
      password: pass
    }

    return this.http.post(this.host + 'api/token/', login)
    .pipe(catchError(this.handleError));
  }

  logout(): boolean {
    localStorage.removeItem('token');
    this.router.navigate(['/login']);
    return true;
  }

  getOptions(): any {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
        Authorization: 'Bearer ' + localStorage.getItem('token')
      })
    };
    return httpOptions;
  }

  
  isLoggedIn() {
    this.loggedIn = !!localStorage.getItem('token');
    return this.loggedIn;
  }

  private handleError(error: HttpErrorResponse) {
    if (error.error instanceof ErrorEvent) {
      console.error('An error occurred:', error.error.message);
    } else {
      console.error(
        `Backend returned code ${error.status}, ` +
        `body was:`);
      console.log(error.error)
    }
    return throwError(error.error);
  }

}
