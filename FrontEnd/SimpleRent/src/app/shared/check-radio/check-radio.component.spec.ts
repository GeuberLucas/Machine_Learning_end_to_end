import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CheckRadioComponent } from './check-radio.component';

describe('CheckRadioComponent', () => {
  let component: CheckRadioComponent;
  let fixture: ComponentFixture<CheckRadioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CheckRadioComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CheckRadioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
