import { Component } from '@angular/core';
import { ApiService } from '../../api/index';

@Component({
    selector: 'app-sidebar',
    templateUrl: './sidebar.component.html',
    styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent {

    constructor(private apiService: ApiService) {

    }

    ngOnInit() {
    }
}
