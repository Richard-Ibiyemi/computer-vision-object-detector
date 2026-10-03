# Practical detection evaluation

## Current evaluation: new photographs, small model

- Model: `yolov8s-oiv7.pt` (YOLOv8 small pretrained on Open Images V7), confirmed by the project author. The uploaded ZIP contains result images, without the script or execution logs.
- Targets: human hand, plastic water bottle and prescription glasses.
- Input set: 12 unique photographs, four conditions per target: normal, dim, obscured and far.
- Thresholds: 0.15, 0.4 and 0.6; 36 annotated outputs inspected.
- Evidence: `test_results_new.zip`, with results in `conf_0.15`, `conf_0.4` and `conf_0.6`.
- The filenames use `sunglasses`, but the photographs show clear-lens prescription glasses. The appropriate target label is `Glasses`.

A target counted as detected when its category was correct and its box reasonably surrounded the visible target. This was a visual check, without ground-truth box annotations or a formal IoU criterion. Duplicate boxes were recorded separately and did not count as additional target successes. Visible-target localisation was accepted for the partially obscured bottle; this does not establish recovery of its hidden extent.

## Summary

| Threshold | Hand | Bottle | Glasses | Targets detected across 12 images |
|---|---:|---:|---:|---:|
| 0.15 | 3/4 | 4/4 | 2/4 | 9/12 |
| 0.4 | 1/4 | 4/4 | 2/4 | 7/12 |
| 0.6 | 0/4 | 1/4 | 2/4 | 3/12 |

These counts describe this small set only. They are not overall model accuracy, precision, recall or mAP. The same 12 photographs are reused at each threshold, so the 36 outputs are not independent test samples.

## Observations

### Bottle

The plastic water bottle was correctly detected in all four photographs at thresholds 0.15 and 0.4. The displayed scores were 0.64 (normal), 0.57 (dim), 0.59 (obscured) and 0.48 (far). At 0.6, only the normal bottle remained. The obscuring object was also correctly labelled `Box` at 0.63 at every threshold. A broad `Table` box appeared in the far image at 0.15, although its localisation extended over the cabinet rather than tightly around the tabletop.

### Hand

The normal, dim and far hand photographs were correctly labelled `Human hand` at 0.15, with scores 0.26, 0.41 and 0.29. At 0.4, only the dim hand remained; at 0.6, none remained. The obscured hand was missed at every threshold. At 0.15, its blocking object received the appropriate `Remote control` label (0.28), but the box was loose and included much of the hand. The sleeve was incorrectly labelled `Jeans` (0.30).

The dim hand scored higher than the normal hand. This does not show that dim lighting improves detection: pose, camera angle and framing differ, and there is only one example of each condition.

### Glasses

The normal and dim glasses photographs were correctly detected at all three thresholds, with scores 0.66 and 0.69. At 0.15, the normal photograph also contained a duplicate, partial glasses box at 0.29. The dim photograph contained a duplicate glasses box at 0.27 and an incorrect `Goggles` label at 0.19 over the same object. Those extra boxes disappeared at 0.4 and 0.6. The obscured and far glasses were missed at every threshold. A background laptop was labelled at 0.23 in the obscured image at 0.15, and a broad table box appeared at 0.26 in the far image.

## Detailed results

Scores are rounded values printed on the output images. A missing target label means that no appropriate target box survived that threshold; other objects can still have detections.

| Image | Threshold | Target detected correctly? | Target label and score | Extra detections / errors | Notes |
|---|---:|---|---|---|---|
| hand_normal.jpg | 0.15 | Yes | Human hand 0.26 | None | Open palm correctly localised at the lowest threshold. |
| hand_normal.jpg | 0.4 | No | None | None | Correct Human hand prediction at 0.26 filtered out by this threshold. |
| hand_normal.jpg | 0.6 | No | None | None | Correct Human hand prediction at 0.26 filtered out by this threshold. |
| hand_dim.jpg | 0.15 | Yes | Human hand 0.41 | None | Hand detected with a higher score than in the normal image; pose/framing also differ. |
| hand_dim.jpg | 0.4 | Yes | Human hand 0.41 | None | Hand detected with a higher score than in the normal image; pose/framing also differ. |
| hand_dim.jpg | 0.6 | No | None | None | Correct Human hand prediction at 0.41 filtered out by this threshold. |
| hand_obscured.jpg | 0.15 | No | None | Remote control 0.28 (loose box); incorrect Jeans 0.30 on sleeve | Remote covers much of the palm; target hand missed. |
| hand_obscured.jpg | 0.4 | No | None | None | Remote covers much of the palm; target hand missed. |
| hand_obscured.jpg | 0.6 | No | None | None | Remote covers much of the palm; target hand missed. |
| hand_far.jpg | 0.15 | Yes | Human hand 0.29 | None | Distant hand detected only at the lowest threshold. |
| hand_far.jpg | 0.4 | No | None | None | Correct Human hand prediction at 0.29 filtered out by this threshold. |
| hand_far.jpg | 0.6 | No | None | None | Correct Human hand prediction at 0.29 filtered out by this threshold. |
| bottle_normal.jpg | 0.15 | Yes | Bottle 0.64 | None | Box reasonably surrounds the full bottle. |
| bottle_normal.jpg | 0.4 | Yes | Bottle 0.64 | None | Box reasonably surrounds the full bottle. |
| bottle_normal.jpg | 0.6 | Yes | Bottle 0.64 | None | Box reasonably surrounds the full bottle. |
| bottle_dim.jpg | 0.15 | Yes | Bottle 0.57 | None | Bottle score is lower than in the normal image. |
| bottle_dim.jpg | 0.4 | Yes | Bottle 0.57 | None | Bottle score is lower than in the normal image. |
| bottle_dim.jpg | 0.6 | No | None | None | Correct Bottle prediction at 0.57 filtered out by this threshold. |
| bottle_obscured.jpg | 0.15 | Yes | Bottle 0.59 | Box 0.63 (correct blocking object) | Box surrounds visible bottle above the blocking box; occluded extent not formally assessed. |
| bottle_obscured.jpg | 0.4 | Yes | Bottle 0.59 | Box 0.63 (correct blocking object) | Box surrounds visible bottle above the blocking box; occluded extent not formally assessed. |
| bottle_obscured.jpg | 0.6 | No | None | Box 0.63 (correct blocking object) | Correct Bottle prediction at 0.59 filtered out by this threshold. |
| bottle_far.jpg | 0.15 | Yes | Bottle 0.48 | Table 0.23 (broad cabinet/table region) | Smaller bottle detected at 0.48. |
| bottle_far.jpg | 0.4 | Yes | Bottle 0.48 | None | Smaller bottle detected at 0.48. |
| bottle_far.jpg | 0.6 | No | None | None | Correct Bottle prediction at 0.48 filtered out by this threshold. |
| sunglasses_normal.jpg | 0.15 | Yes | Glasses 0.66 | Duplicate Glasses 0.29 around front frame/lenses | Clear-lens prescription glasses correctly labelled Glasses. |
| sunglasses_normal.jpg | 0.4 | Yes | Glasses 0.66 | None | Clear-lens prescription glasses correctly labelled Glasses. |
| sunglasses_normal.jpg | 0.6 | Yes | Glasses 0.66 | None | Clear-lens prescription glasses correctly labelled Glasses. |
| sunglasses_dim.jpg | 0.15 | Yes | Glasses 0.69 | Duplicate Glasses 0.27; incorrect Goggles 0.19 | Glasses detected at 0.69; slightly different framing from normal. |
| sunglasses_dim.jpg | 0.4 | Yes | Glasses 0.69 | None | Glasses detected at 0.69; slightly different framing from normal. |
| sunglasses_dim.jpg | 0.6 | Yes | Glasses 0.69 | None | Glasses detected at 0.69; slightly different framing from normal. |
| sunglasses_obscured.jpg | 0.15 | No | None | Laptop 0.23 (background) | Remote overlaps the lower glasses region; target missed. |
| sunglasses_obscured.jpg | 0.4 | No | None | None | Remote overlaps the lower glasses region; target missed. |
| sunglasses_obscured.jpg | 0.6 | No | None | None | Remote overlaps the lower glasses region; target missed. |
| sunglasses_far.jpg | 0.15 | No | None | Table 0.26 (broad cabinet/table region) | Small distant glasses missed at all tested thresholds. |
| sunglasses_far.jpg | 0.4 | No | None | None | Small distant glasses missed at all tested thresholds. |
| sunglasses_far.jpg | 0.6 | No | None | None | Small distant glasses missed at all tested thresholds. |

## Threshold interpretation

Threshold 0.15 retained the most intended targets, but also retained duplicate boxes and incorrect labels. Threshold 0.4 removed those observed duplicate glasses boxes and low-confidence mistakes while retaining all four bottles and the normal/dim glasses. It also discarded the normal and far hand detections. Threshold 0.6 discarded most correct hand and bottle predictions and retained only three targets.

For this set, 0.4 is a reasonable starting point for a cleaner webcam display; 0.15 is worth testing if recovering hands is the priority. Neither choice is established as generally optimal from these 12 images. Keep recording misses and false positives during live use.

Changing the threshold filters existing predictions; it does not change the learned categories or teach the model to correct mistakes. A confidence score is not an accuracy percentage.

## Limitations

- One physical example per category and one photograph per condition provide limited evidence of generalisation.
- The new scenes are less cluttered, but camera angle, framing and object pose still differ between conditions.
- Lighting levels, distances and occlusion percentages were not measured. Condition names describe the intended tests.
- The earlier drinks bottle was replaced with a different plastic bottle. Changes across sets cannot be attributed solely to the background or model.
- No IoU-based evaluation or exhaustive annotations for background objects were supplied. Box quality was assessed visually.
- The model name is author-confirmed; package versions, image size and inference device still need to be recorded from the running environment.
- Webcam screenshots provide sampled processing-FPS readings on battery power and plugged in, not sustained throughput or end-to-end latency measurements.

## Earlier exploratory tests

The earlier nano-model notes described 12 classroom/carpet photographs with no successful target detections at the three tested thresholds. A later run, confirmed by the author as the small model, detected the normal glasses at 0.36 at threshold 0.15, while the hand and bottle targets remained missed. Those scenes used different framing, backgrounds and a different bottle from the current set. They are retained as exploratory failure observations, not a controlled model benchmark.

## Webcam speed: laptop on battery power

The replacement screenshots in `t(1).zip` were captured on an unplugged laptop. The first five are assigned to image size 640 and the last five to 320, following the previously confirmed capture order. Confidence was set to 0.4 as reported by the author. The model used in the project is `yolov8s-oiv7.pt`; a running script/log was not included to independently verify the settings.

| Image size | FPS 1 | FPS 2 | FPS 3 | FPS 4 | FPS 5 | Mean processing FPS | Detection observations |
|---|---:|---:|---:|---:|---:|---:|---|
| 640 | 9.4 | 8.8 | 9.3 | 9.0 | 8.8 | 9.06 | Bottle detected in all five saved frames; scores 0.60, 0.61, 0.63, 0.59 and 0.60. |
| 320 | 9.1 | 9.5 | 9.1 | 8.9 | 8.7 | 9.06 | Bottle detected in all five saved frames; scores 0.60, 0.60, 0.61, 0.60 and 0.61. |

Both sets have the same mean, 9.06 processing FPS, with overlapping ranges (8.8–9.4 at 640 and 8.7–9.5 at 320). These samples show no measured speed advantage for 320 in this battery-powered run. They do not establish that the two sizes always perform identically or confirm the actual inference tensor sizes.

The scene and bottle placement are visually similar between the two groups. The bottle is detected in all ten saved frames, but that does not establish uninterrupted detection throughout the video. No extra detection boxes are visible in these saved frames. The screenshot filenames indicate irregular sampling intervals of roughly 4–8 seconds, rather than exactly 10 seconds. The warm-up duration was not verified.

The displayed value is a smoothed processing-FPS estimate from the supplied webcam implementation, covering camera capture, prediction and annotation. It excludes display time and is not a full end-to-end latency benchmark. Averaging five displayed readings is a small practical check, not a sustained frame-count/time benchmark.

## Webcam speed: laptop plugged in

The ten screenshots in `t(2).zip` were captured with the laptop plugged in. In filename/timestamp order, the first five are assigned to image size 640 and the last five to 320, following the author's capture plan. The configured model is `yolov8s-oiv7.pt` and confidence threshold is 0.4. These settings are author-reported; the screenshots do not independently verify the actual inference tensor sizes.

| Image size | FPS 1 | FPS 2 | FPS 3 | FPS 4 | FPS 5 | Mean processing FPS | Detection observations |
|---|---:|---:|---:|---:|---:|---:|---|
| 640 | 15.9 | 16.1 | 15.1 | 15.5 | 16.3 | 15.78 | Bottle detected in all five saved frames; scores 0.57, 0.44, 0.53, 0.53 and 0.45. |
| 320 | 43.8 | 44.7 | 42.9 | 42.1 | 42.1 | 43.12 | Bottle visible, but no detection boxes displayed in any of the five saved frames at threshold 0.4. |

At 320, the mean displayed processing rate was approximately 2.73 times the rate at 640. This speed gain came with a missed bottle in all five saved frames at the configured threshold. These observations demonstrate a practical speed/detection tradeoff for this scene; they do not establish overall detection accuracy or show whether bottle predictions existed below 0.4.

The framing is similar between the two plugged-in groups. It differs from the battery-powered test, as the author noted, so the power-condition comparison is not fully controlled. The plugged-in readings are higher than the recorded battery readings, but laptop power mode, thermal state and the cause of the difference were not measured.

These are five samples of a smoothed processing-FPS display per setting, not sustained video benchmarks or end-to-end display FPS. Filename timestamps indicate approximately 5–6 seconds between the 640 samples and 2–3 seconds between the 320 samples. Warm-up duration was not verified. Detection counts refer only to saved frames, not uninterrupted detection throughout the video.

### Demonstration setting

Use the laptop plugged in with image size 640 and confidence 0.4 for the bottle demonstration. In this run, this setting retained the bottle in all five saved frames at a mean of 15.78 processing FPS. Size 320 was faster but did not display the bottle detection at the same threshold. These results are sufficient for this practical comparison; no replacement set is needed merely because 320 missed the bottle.

## Recorded webcam demonstration

Evidence: `webcam_demo.mp4.mp4`, a 31.2-second screen recording. For the repository, rename it to `webcam_demo.mp4` and place it in `docs/`. The author reported completing the demonstration setup with the laptop plugged in, model `yolov8s-oiv7.pt`, image size 640 and confidence 0.4; the recording itself does not display all configuration settings.

Representative frames sampled approximately every two seconds show the bottle being moved, raised and tilted by hand. `Bottle` boxes appear at multiple positions, with sampled displayed confidence scores including 0.56, 0.64, 0.51 and 0.49. Some sampled frames show the visible bottle without a bottle box, so detection is intermittent during movement. This demonstrates live detection and reacquisition, but does not establish continuous object tracking or identify why each miss occurred.

`Person` and `Clothing` boxes also appear over the person holding the bottle. Some boxes overlap and vary in extent. The visible hand does not consistently receive its own `Human hand` label in the sampled frames.

The processing-FPS overlay is mostly around 13–15 in the sampled frames after an early reading of 9.7. This is a qualitative observation from the demonstration, not a new five-reading benchmark or an average over all video frames. The previous plugged-in averages (15.78 at 640 and 43.12 at 320) remain separate. The video file's encoded frame rate is not the detector's processing rate.

The recording provides a usable demonstration of the application, including its detection gaps. No frame-by-frame ground-truth annotation was performed, so no video accuracy or detection-success percentage is reported.

## Run details to complete

- Python version: 3.14.5
- Ultralytics version: 8.4.171
- Image-evaluation inference size: 640
- Laptop CPU/GPU: i7-13700HX / NVIDIA GeForce RTX 4060 Laptop GPU
- Inference device (CPU or GPU): CPU
- Webcam model: `yolov8s-oiv7.pt` (YOLOv8 small), confirmed in `detect_webcam.py`.
- Webcam confidence threshold: 0.4, confirmed in `detect_webcam.py`.
- Webcam speed results: mean 9.06 processing FPS at each tested image size on battery power; plugged-in means 15.78 at 640 and 43.12 at 320.
