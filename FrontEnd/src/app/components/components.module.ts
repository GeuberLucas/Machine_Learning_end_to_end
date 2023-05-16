import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NavbarComponent } from './navbar/navbar.component';
import { ErrorDynamicComponent } from './error-dynamic/error-dynamic.component';
import { MenubarModule } from 'primeng/menubar';


@NgModule({
  declarations: [
    NavbarComponent,
    ErrorDynamicComponent
  ],
  imports: [
    CommonModule,
    MenubarModule
  ],
  exports:[
    NavbarComponent,
    ErrorDynamicComponent
  ]
})
export class ComponentsModule { }
