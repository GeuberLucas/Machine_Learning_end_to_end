import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { InputComponent } from './input/input.component';
import { SelectComponent } from './select/select.component';
import { CheckRadioComponent } from './check-radio/check-radio.component';



@NgModule({
  declarations: [
    InputComponent,
    SelectComponent,
    CheckRadioComponent
  ],
  imports: [
    CommonModule
  ]
})
export class SharedModule { }
