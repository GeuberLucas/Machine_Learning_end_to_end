import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ErrorDynamicComponent } from './error-dynamic.component';

describe('ErrorDynamicComponent', () => {
  let component: ErrorDynamicComponent;
  let fixture: ComponentFixture<ErrorDynamicComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ErrorDynamicComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ErrorDynamicComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
