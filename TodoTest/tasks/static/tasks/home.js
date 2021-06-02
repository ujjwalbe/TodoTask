$(document).ready(function () {
    // const taskDiv = document.getElementById("task");
    const taskDiv = document.getElementsByClassName("task-card")
    for (var i =0; i < taskDiv.length; i++){
        taskDiv[i].addEventListener("click", function(e){
            alert(`You clicked me! ${e.target.id}`)
        });
    }
function replyMe(id){
    console.log(id);
    alert(id);
}

//     const userType = document.getElementById("id_user_type");
//   const bottomForm = $("#below-form");
//   const errResponse = $('#errorResponseTemplate');
  
//   errResponse.hide();
//     const country = jQuery('#id_country').select2({
//       placeholder: "Select Country",
//       // allowClear: true,
//     });
  
//     const segments = jQuery('#id_segment').select2({
//       placeholder: "Select Segments"
//     })
  
//   const userTypeSec = jQuery('#id_user_type').select2({
//     placeholder: "Select User Type"
//   })
//     const packages = jQuery('#id_package').select2({
//       placeholder: "Select Packages"
//     })
//     bottomForm.hide();
//     document.getElementById("submit-button").disabled = true;
  
//     // GETS PINCODE 
//     const pincode = jQuery('#id_pincode').select2({
//       placeholder: 'Select Pincode',
//       allowClear: true,
//       minimumInputLength: 2,
//       ajax: {
//         url: '/api/v1/locations/pincode/',
//         data: function (params) {
//           var query = {
//             q: params.term,
//             country: country.val(),
//             type: 'public'
//           }
  
//           // Query parameters will be ?search=[term]&type=public
//           return query;
//         },
//         processResults: function (data) {
//           // Transforms the top-level key of the response object from 'items' to 'results'
//           const results = data.results;
//           var dataUpdated = $.map(results, function (obj) {
//             obj.text = obj.text || obj.name; // replace name with the property used for the text
  
//             return obj;
//           });
//           return {
//             results: dataUpdated
//           };
//         }
//       }
//     });
  
//     const state = jQuery('#id_state');
  
//     const district = jQuery('#id_district');
  
//     function loadSegment() {
//           const url = "/api/v1/models/segments/"
//           items = []
//           $.ajax({
//           url: url,
//           success: function (data) {
//             const results = data.results;
//             pincodes = results;
  
//             items.push(`<option value="">Select Segments</option>`);
//             console.log(data)
//             if (data.count >= 1) {
//               for (let result of results) {
//                 const output = `<option value="${result.id}">${result.segment_name}  - (${result.description})</option>`;
//                 items.push(output);
//               }
//             }
//             segments.html(items);
//           },
//           error: function (error) {
//             console.log(error);
//           }
//         });
//     }
//     loadSegment();
  
//   function loadUserType() {
//     const url = "/api/v1/users/user-type/"
//     userTypeItems = []
//     $.ajax({
//     url: url,
//     success: function (data) {
//       const results = data.results;
//       pincodes = results;
  
//       userTypeItems.push(`<option value="">Select UserType</option>`);
//       console.log(data)
//       if (data.count >= 1) {
//         for (let result of results) {
//           const output = `<option value="${result.id}">${result.name}  - (${result.description})</option>`;
//           userTypeItems.push(output);
//         }
//       }
//       userTypeSec.html(userTypeItems);
//     },
//     error: function (error) {
//       console.log(error);
//     }
//   });
//   }
//   loadUserType();
  
//     // PINCODE
//     pincode.change(function (e) {
//       const $this = $(this);
//       const value = $this.val();
//       let stateItem = "";
//       let districtItem = "";
  
//       if (value !== '') {
//         var url = `/api/v1/locations/pincode/${value}/`;
  
//         $.ajax({
//           url: url,
//           success: function (data) {
//             const results = data;
//             const districtData = results.district;
//             const stateData = districtData.state;
  
//             districtData !== undefined ? district.val(districtData.name) : district.val("");
//             stateData !== undefined ? state.val(stateData.name) : state.val("");
  
//           },
//           error: function (error) {
//             console.log(error);
//           }
//         });
  
//       } else {
//         state.val("");
//         district.val("");
  
//       }
//     });
  
//     let packagesList = [];
  
//     const packageTemplate = (data) => {
//       const output = `<div class="card">
//           <div class="card-body text-center">
//               <h4 class="mt-2 mb-3"><span>Name: </span>${data.code}</h4>
//               <h5 class="mt-2 mb-3"><span>Description: </span>${data.description}</h5>
//           </div>
//       </div>`;
//       return output;
//     }
  
//     const $id_package = jQuery('#id_package');
  
//     // COUNTRTY
//     country.change(function (e) {
//       const $this = $(this);
//       const value = $this.val();
//       let items = [];
  
//       // $('#id_package').prop("disabled", false);
//       $('#id_pincode').prop("disabled", false);
  
//       if (value !== '') {
//         var url = `/api/v1/locations/pincode/?country=${value}`;
  
//         $.ajax({
//           url: url,
//           success: function (data) {
//             const results = data.results;
//             pincodes = results;
  
//             items.push(`<option value="">Select Pincode</option>`);
//             console.log(data)
//             if (data.count >= 1) {
//               for (let result of results) {
//                 const output = `<option value="${result.id}">${result.name}</option>`;
//                 items.push(output);
//               }
//             }
//            pincode.html(items);
//           },
//           error: function (error) {
//             console.log(error);
//           }
//         });
  
//       } else {
//         pincode.html(items);
//       }
//     });
  
//     // STATE
  
//     state.change(function (e) {
//       const $this = $(this);
//       const value = $this.val();
//       let items = [];
  
//       // $('#id_package').prop("disabled", false);
//       $('#id_pincode').prop("disabled", false);
  
//       if (value !== '') {
//         var url = `/api/v1/locations/pincode/?country=${value}`;
  
//         $.ajax({
//           url: url,
//           success: function (data) {
//             const results = data.results;
//             pincodes = results;
  
//             items.push(`<option value="">Select Pincode</option>`);
//             console.log(data)
//             if (data.count >= 1) {
//               for (let result of results) {
//                 const output = `<option value="${result.id}">${result.name}</option>`;
//                 items.push(output);
//               }
//             }
//            pincode.html(items);
//           },
//           error: function (error) {
//             console.log(error);
//           }
//         });
  
//       } else {
//         pincode.html(items);
//       }
//     });
  
  
//     // $id_package.change(function (e) {
//     //   const $this = $(this);
//     //   const value = $this.val();
  
//     //   let selectedPackage = packagesList.find(function (item, index) {
//     //     if (item.id == value)
//     //       return true;
//     //   });
  
//     //   if (selectedPackage !== undefined) {
//     //     const output = packageTemplate(selectedPackage);
//     //     responseTemplate.html(output);
//     //   } else {
//     //     responseTemplate.html('');
//     //   }
  
//     // });
  
//   // sort by segments country user_type
//     // ############# button click function
//     getPackage.addEventListener('click', function () {
//       console.log("click");
//       let countryVal = country.val();
//       let segmentVal = segments.val();
//       let usertypeVal = userType.value;
//       let pincodeVal = pincode.val();
//       console.log(countryVal, usertypeVal, segmentVal)
//       $('#id_package').prop("disabled", false);
//       var url = `/api/v1/packages/list/?country=${countryVal}&segment=${segmentVal}&type_id=${usertypeVal}&active=True&vis=Public`;
//       let items = [];
//       if (segmentVal == ''){
//         alert("Please select Vehicle Segment")
//         return ;
//       }
//       if(usertypeVal == ''){
//         alert("Please select User Type")
//         return;
//       }
//       if (countryVal == ''){
//         alert("Please select country")
//         return;
//       }
//       if(pincodeVal == ''){
//         alert("Please select pincode");
//         return;
//       }
      
  
//         $.ajax({
//           url: url,
//           success: function (data) {
//             const results = data.results;
//             packagesList = results;
            
//             items.push(`<option value="">Select Package</option>`);
//             console.log(data)
//             if (data.count === 0){
//               errResponse.show();
//               bottomForm.hide();
//               document.getElementById("submit-button").disabled = true;
//             }
//             if (data.count >= 1) {
//               bottomForm.show();
//               errResponse.hide();
  
//               document.getElementById("submit-button").disabled = false;
//               for (let result of results) {
//                 const output = `<option value="${result.id}">${result.code}</option>`;
//                 items.push(output);
//               }
//             }
//             $id_package.html(items);
//           },
//           error: function (error) {
//             console.log(error);
//           }
//         });
  
//     })
  
  
//     // $country.change(function (e) {
//     //   const $this = $(this);
//     //   const value = $this.val();
//     //   let items = [];
  
//     //   $('#id_package').prop("disabled", false);
//     //   console.log('hhhhh')
  
//     //   if (value !== '') {
//     //     var url = `/api/v1/packages/list/?country=${value}&segment=1`;
  
//     //     $.ajax({
//     //       url: url,
//     //       success: function (data) {
//     //         const results = data.results;
//     //         packagesList = results;
  
//     //         items.push(`<option value="">Select Package</option>`);
  
//     //         if (data.count >= 1) {
//     //           for (let result of results) {
//     //             const output = `<option value="${result.id}">${result.code}</option>`;
//     //             items.push(output);
//     //           }
//     //         }
//     //         $id_package.html(items);
//     //       },
//     //       error: function (error) {
//     //         console.log(error);
//     //       }
//     //     });
  
//     //   } else {
//     //     $id_package.html(items);
//     //   }
//     // });
  
  
//     $id_package.change(function (e) {
//       const $this = $(this);
//       const value = $this.val();
  
//       let selectedPackage = packagesList.find(function (item, index) {
//         if (item.id == value)
//           return true;
//       });
  
//       if (selectedPackage !== undefined) {
//         const output = packageTemplate(selectedPackage);
//         responseTemplate.html(output);
//       } else {
//         responseTemplate.html('');
//       }
  
//     });
  
  
  });
  