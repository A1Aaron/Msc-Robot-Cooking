
"use strict";

let GetCoords = require('./GetCoords.js')
let PumpStatus = require('./PumpStatus.js')
let GetAngles = require('./GetAngles.js')
let GripperStatus = require('./GripperStatus.js')
let SetAngles = require('./SetAngles.js')
let SetCoords = require('./SetCoords.js')

module.exports = {
  GetCoords: GetCoords,
  PumpStatus: PumpStatus,
  GetAngles: GetAngles,
  GripperStatus: GripperStatus,
  SetAngles: SetAngles,
  SetCoords: SetCoords,
};
