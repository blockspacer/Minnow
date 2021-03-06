// automatically generated by the FlatBuffers compiler, do not modify


#ifndef FLATBUFFERS_GENERATED_NAVTOPIC1_TOPICS_NAV_H_
#define FLATBUFFERS_GENERATED_NAVTOPIC1_TOPICS_NAV_H_

#include "flatbuffers/flatbuffers.h"

namespace topics {
namespace nav {

struct topic1;

struct topic1 FLATBUFFERS_FINAL_CLASS : private flatbuffers::Table {
  enum FlatBuffersVTableOffset FLATBUFFERS_VTABLE_UNDERLYING_TYPE {
    VT_TIME = 4,
    VT_TEST = 6
  };
  double time() const {
    return GetField<double>(VT_TIME, 0.0);
  }
  const flatbuffers::String *test() const {
    return GetPointer<const flatbuffers::String *>(VT_TEST);
  }
  bool Verify(flatbuffers::Verifier &verifier) const {
    return VerifyTableStart(verifier) &&
           VerifyField<double>(verifier, VT_TIME) &&
           VerifyOffset(verifier, VT_TEST) &&
           verifier.VerifyString(test()) &&
           verifier.EndTable();
  }
};

struct topic1Builder {
  flatbuffers::FlatBufferBuilder &fbb_;
  flatbuffers::uoffset_t start_;
  void add_time(double time) {
    fbb_.AddElement<double>(topic1::VT_TIME, time, 0.0);
  }
  void add_test(flatbuffers::Offset<flatbuffers::String> test) {
    fbb_.AddOffset(topic1::VT_TEST, test);
  }
  explicit topic1Builder(flatbuffers::FlatBufferBuilder &_fbb)
        : fbb_(_fbb) {
    start_ = fbb_.StartTable();
  }
  topic1Builder &operator=(const topic1Builder &);
  flatbuffers::Offset<topic1> Finish() {
    const auto end = fbb_.EndTable(start_);
    auto o = flatbuffers::Offset<topic1>(end);
    return o;
  }
};

inline flatbuffers::Offset<topic1> Createtopic1(
    flatbuffers::FlatBufferBuilder &_fbb,
    double time = 0.0,
    flatbuffers::Offset<flatbuffers::String> test = 0) {
  topic1Builder builder_(_fbb);
  builder_.add_time(time);
  builder_.add_test(test);
  return builder_.Finish();
}

inline flatbuffers::Offset<topic1> Createtopic1Direct(
    flatbuffers::FlatBufferBuilder &_fbb,
    double time = 0.0,
    const char *test = nullptr) {
  auto test__ = test ? _fbb.CreateString(test) : 0;
  return topics::nav::Createtopic1(
      _fbb,
      time,
      test__);
}

inline const topics::nav::topic1 *Gettopic1(const void *buf) {
  return flatbuffers::GetRoot<topics::nav::topic1>(buf);
}

inline const topics::nav::topic1 *GetSizePrefixedtopic1(const void *buf) {
  return flatbuffers::GetSizePrefixedRoot<topics::nav::topic1>(buf);
}

inline bool Verifytopic1Buffer(
    flatbuffers::Verifier &verifier) {
  return verifier.VerifyBuffer<topics::nav::topic1>(nullptr);
}

inline bool VerifySizePrefixedtopic1Buffer(
    flatbuffers::Verifier &verifier) {
  return verifier.VerifySizePrefixedBuffer<topics::nav::topic1>(nullptr);
}

inline void Finishtopic1Buffer(
    flatbuffers::FlatBufferBuilder &fbb,
    flatbuffers::Offset<topics::nav::topic1> root) {
  fbb.Finish(root);
}

inline void FinishSizePrefixedtopic1Buffer(
    flatbuffers::FlatBufferBuilder &fbb,
    flatbuffers::Offset<topics::nav::topic1> root) {
  fbb.FinishSizePrefixed(root);
}

}  // namespace nav
}  // namespace topics

#endif  // FLATBUFFERS_GENERATED_NAVTOPIC1_TOPICS_NAV_H_
