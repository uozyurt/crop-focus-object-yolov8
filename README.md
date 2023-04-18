# crop-focus-object-yolov8
This project is useful only for pre-trained yolov8 weights. It requires a weights file ("xxx.pt") and images to crop.

"crop_focus_object_driver.py" file is an example for using the crop function. You need to declare the paths of images and weight.pt file.

"choose_one_bbox.py" has a function which decides the bounding box which is most likely to be the focus object bbox in case of multiple detections.

Requirements that have to be installed:

ultralytics <br />
cv2 <br />
os <br />
imageio <br />
pytorch <br />
time <br />

### Here are some input-output examples of the crop function. (0.01 margin used)



Example 1 input: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750178-3b9ddbae-2a1c-4129-b23a-fd7bdf17bac9.jpeg" width=45% /> <br />
Example 1 output: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750273-1043e235-26e1-444d-9e1e-1c1698dd5592.jpeg" width=20% />

Example 2 input: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750186-8df9c73f-1c71-498c-902b-3d7e9601afe8.jpeg" width=45% /> <br />
Example 2 output: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750310-edbbdccb-06e0-4cb5-9aa0-6b594c285b3b.jpeg" width=20% />


Example 3 input: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750187-4c56a408-6984-4789-a5c9-ad0a70f0ab49.jpeg" width=45% /> <br />
Example 3 output: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750324-1968f973-37f6-419f-8ce5-731793670d39.jpeg" width=20% />

Example 4 input: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750189-bc68bcfa-7a13-4d85-90c1-24490c008362.jpeg" width=45% /> <br />
Example 4 output: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750354-4d703631-7c6e-4ce6-9200-1d249f728169.jpeg" width=20% />


Example 5 input: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750192-e3047605-0a00-40cd-b8ce-2994bad447a4.jpeg" width=45% /> <br />
Example 5 output: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750379-8ddfb1df-a210-42a0-b4d0-6ccd49c87ead.jpeg" width=20% />


Example 6 input: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750194-bfc830c2-f4bf-4f24-957f-ad85aba605ca.jpeg" width=45% /> <br />
Example 6 output: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750450-31e0569c-13ee-4f0e-b6b6-2f3f9503a47d.jpeg" width=20% />


Example 7 input: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750195-14adfae2-4e0b-49b1-a988-584e148fe15e.jpeg" width=45% /> <br />
Example 7 output: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750464-354c87d3-8994-427c-8f6b-0bb70255fb45.jpeg" width=20% />


Example 8 input: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750198-351b17f2-e85c-4eb2-92aa-1bb4e3f0d0ae.jpeg" width=45% /> <br />
Example 8 output: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750481-2ff1ebb6-6434-469f-955b-96a600bd0a37.jpeg" width=20% />


Example 9 input: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750202-3fba9011-4907-4770-8547-4c75798591db.jpeg" width=45% /> <br />
Example 9 output: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750500-4f9ce103-143f-4889-abc2-8c216fda697b.jpeg" width=20% />


Example 10 input: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750207-b1a71f17-1f22-4e23-b5fd-3f4f0079a557.jpeg" width=45% /> <br />
Example 10 output: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750509-b95aac91-e7b3-4d9a-9005-fbc07d5568ef.jpeg" width=20% />

Example 11 input: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750211-54be355c-48e1-4f9b-b06e-4c1bfa270b96.jpeg" width=45% /> <br />
Example 11 output: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750530-3dc833fd-ad52-40a8-84f7-67666481d673.jpeg" width=20% />


Example 12 input: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750217-da173c0e-1e9d-4bc3-8189-243b1c543ee8.jpeg" width=45% /> <br />
Example 12 output: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750544-38faa8d0-2e03-4565-a2aa-091335c8ced6.jpeg" width=20% />


Example 13 input: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750218-e46aca4b-55f2-4d7d-ae80-7b1460b23850.jpeg" width=45% /> <br />
Example 13 output: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750553-d62e3980-a519-4a0c-b55a-86c43fa0fb81.jpeg" width=20% />


Example 14 input: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750223-0f1a2159-033d-4476-a262-fd0dda18ccee.jpeg" width=45% /> <br />
Example 14 output: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750562-ba47e090-05fb-40be-bf60-ff461e2b98f9.jpeg" width=20% />


Example 15 input: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750228-a69ba789-189b-43b6-a964-a74044a9de99.jpeg" width=45% /> <br />
Example 15 output: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750573-a5e843fb-5261-4d19-8194-07e7f80296e0.jpeg" width=20% />


Example 16 input: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750235-d8107ffe-089f-4790-baa6-ffd313f23716.jpeg" width=45% /> <br />
Example 16 output: <br />
<img src="https://user-images.githubusercontent.com/125663669/232750585-d65d3209-e248-4745-bf9e-3ca5e072cf7d.jpeg" width=20% />



