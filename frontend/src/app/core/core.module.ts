import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent, FooterComponent, SidebarComponent } from '../shared';
import { CoreRoutingModule } from './core-routing.module';
import { CoreComponent } from './core.component';
import {FormsModule} from "@angular/forms";  

@NgModule({
  declarations: [
  	CoreComponent,
  	HeaderComponent,
  	FooterComponent,
  	SidebarComponent
  ],
  imports: [
    CommonModule,
    CoreRoutingModule,
    FormsModule
  ]
})
export class CoreModule { }
