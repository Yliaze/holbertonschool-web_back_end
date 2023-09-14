export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    return new this.constructor(
      this[Symbol.for('brand')],
      this[Symbol.for('motor')],
      this[Symbol.for('color')],
    );
  }
}
