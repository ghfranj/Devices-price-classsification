package com.example.springbootproject.controller;

import com.example.springbootproject.entity.Device;
import com.example.springbootproject.service.DeviceService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/devices")
public class DeviceController {

    @Autowired
    private DeviceService deviceService;

    @GetMapping
    public List<Device> getAllDevices() {
        return deviceService.getAllDevices();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Device> getDeviceById(@PathVariable Long id) {
        return deviceService.getDeviceById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public Device addDevice(@RequestBody Device device) {
        return deviceService.addDevice(device);
    }

    @PostMapping("/predict/{deviceId}")
    public ResponseEntity<Device> predictDevicePrice(@PathVariable Long deviceId) {
        return deviceService.getDeviceById(deviceId)
                .map(device -> {
                    int predictedPriceRange = deviceService.predictDevicePrice(device);
                    Device updatedDevice = deviceService.updateDevicePriceRange(deviceId, predictedPriceRange);
                    return ResponseEntity.ok(updatedDevice);
                })
                .orElse(ResponseEntity.notFound().build());
    }
}
